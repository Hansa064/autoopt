"""
The base class for the different distribution decorators.

This module implements an abstract base class for the different
distributions defined in this package. Each distribution
can be used as a decorator, to decorate the hyperparameters
of the different algorithms.

    @Uniform("nu", 0, 1)
    def function_(nu):
        pass

    @Normal("gamma", 0, 1)
    class Algorithm(object):
        def __init__(gamma):
            pass

To help the algorithm experts define good default values,
each distribution can be plotted if the "plotting" extra
is installed. This plots the PDF (probability density function).

    Uniform("nu", 0, 1).plot()
"""
import abc
import copy
import numpy


class Distribution(object, metaclass=abc.ABCMeta):
    """
    Abstract base class for creating distribution decorators.
    By decorating a parameters using a subclass of this, it is defined as
    a parameter to be optimized during the optimization process.

    BE CAREFUL WHEN IMPLEMENTING NEW DECORATORS. THEY HAVE TO BE SUPPORTED
    BY __ALL__ OPTIMIZATION ALGORITHMS
    """
    PARAMETER_CLASS_ATTRIBUTE = "_hyperparameters"

    def __init__(self, parameter_name):
        self._name = parameter_name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def plot(self):
        raise NotImplementedError("Has to be implemented by the subclasses")

    def __call__(self, obj):
        if not hasattr(obj, self.PARAMETER_CLASS_ATTRIBUTE):
            setattr(obj, self.PARAMETER_CLASS_ATTRIBUTE, dict())
        # Copy the attribute to avoid overwriting inherited parameters.
        parameters = copy.copy(getattr(obj, self.PARAMETER_CLASS_ATTRIBUTE))
        parameters[self.name] = self
        setattr(obj, self.PARAMETER_CLASS_ATTRIBUTE, parameters)

    def __eq__(self, other):
        if hasattr(other, "name"):
            return self.name == other.name
        return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{self.__class__.__name__}<{self.name}>".format(self=self)


class QMixin(object):
    """
    This mixin adds a regulation parameter `q`
    to bind a distribution to discrete values.
    """

    def __init__(self, q):
        """
        Add the new regulation parameter.

        :param q: The regulation value
        :type q: float
        """
        self.__q = q

    @property
    def q(self):
        return self.__q

    def round_to_q(self, value):
        """
        Round a value to the next multiple of `q`.
        This is required for the plotting only.

        :param value: The value to round
        :type value: float
        """
        return numpy.round(value / self.q) * self.q
