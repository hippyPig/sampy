from sfunctions import quad

################################################################################
class Error(object):
    def __init__(self, val, err):
        self.val = float(val)
        self.err = float(err)
    def frac(self):
        return self.err / self.val
    def __add__(self, val):
        if isinstance(val, Error):
            self.val += val.val
            self.err = quad(self.err, val.err)
        else:
            self.val += val
        return self
    def __sub__(self, val):
        if isinstance(val, Error):
            self.val -= val.val
            self.err = quad(self.err, val.err)
        else:
            self.val -= val
        return self
    def __mul__(self, val):
        if isinstance(val, Error):
            self.err = quad(self.frac(), val.frac())
            self.val *= val.val
            self.err *= self.val
        else:
            self.val *= val
            self.err *= val
        return self
    def __div__(self, val):
        if isinstance(val, Error):
            self.err = quad(self.frac(), val.frac())
            self.val /= val.val
            self.err *= self.val
        else:
            self.val /= val
            self.err /= val
        return self
    def __pow__(self, val):
        self.err = self.frac() * abs(val)
        self.val = self.val**val
        self.err *= self.val
        return self


class SError(object):
    def __init__(self, centre, err1, err2=None):
        self.upper = Error(centre, err1)
        self.lower = Error(centre, err2 if err2 is not None else err1)
        self.sf = ':.2f'
        self.pow = 0
    ############################################################################
    @property
    def sigfig(self):
        return self.sf
    @sigfig.setter
    def sigfig(self, sf):
        if isinstance(sf, str):
            self.sf = sf
            if not self.sf.startswith(':'):
                self.sf = ':' + self.sf
        else:
            self.sf = ':.{0}f'.format(sf)
        return
    @property
    def power(self):
        return self.pow
    @power.setter
    def power(self, val):
        self.pow = int(val)
        self.upper *= 10**self.pow
        self.lower *= 10**self.pow
        return
    ############################################################################
    def __add__(self, var):
        if isinstance(var, SError):
            self.upper += var.upper
            self.lower += var.lower
        else:
            self.upper += var
            self.lower += var
        return self
    def __sub__(self, var):
        if isinstance(var, SError):
            self.upper -= var.upper
            self.lower -= var.lower
        else:
            self.upper -= var
            self.lower -= var
        return self
    def __mul__(self, var):
        if isinstance(var, SError):
            self.upper *= var.upper
            self.lower *= var.lower
        else:
            self.upper *= var
            self.lower *= var
        return self
    def __div__(self, var):
        if isinstance(var, SError):
            self.upper /= var.upper
            self.lower /= var.lower
        else:
            self.upper /= var
            self.lower /= var
        return self
    def __pow__(self, var):
        self.upper * self.upper ** var
        self.lower * self.lower ** var
        return self
    def __str__(self):
        """Note that {{ and }} are converted to { and } by format()"""
        st_cen = ('{0' + self.sf + '}').format(self.upper.val)
        st_upper = ('{0' + self.sf + '}').format(self.upper.err)
        st_lower = ('{0' + self.sf + '}').format(self.lower.err)
        if self.upper.err == self.lower.err:
            st = st_cen + ' \pm ' + st_upper
        else:
            st = st_cen + ' \,^{+' + st_upper + '}_{-' + st_lower + '}'
        if self.pow != 0:
            st = '({0}) \e{{{1}}}'.format(st, self.pow)
        return st
    def __radd__(self, other):
        return self.__add__(other)
    def __repr__(self):
        return self.__str__()
    ############################################################################


################################################################################
if __name__ == "__main__":
    """TEST"""
















