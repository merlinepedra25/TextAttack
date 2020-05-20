from textattack.shared.utils import default_class_repr
from textattack.constraints import Constraint

class PreTransformationConstraint(Constraint):
    """ 
    An abstract class that represents constraints which are applied before
    the transformation. These restrict which words are allowed to be modified
    during the transformation. For example, we might not allow stopwords to be
    modified.
    """
   
    def __call__(self, x, transformation):
        """ 
        Returns the word indices in ``x`` which are able to be modified. First checks compatibility
        with ``transformation`` then calls ``_get_modifiable_indices``\.

        Args:
            x: The ``TokenizedText`` input to consider.
            transformation: The ``Transformation`` which will be applied.
        """
        if not self.check_compatibility(transformation):
            return set(range(len(x.words)))
        return self._get_modifiable_indices(x)

    def _get_modifiable_indices(x):
        """
        Returns the word indices in x which are able to be modified. Must be overridden by 
        specific pre-transformation constraints.

        Args:
            x: The ``TokenizedText`` input to consider.
        """
        raise NotImplementedError()
