import hilbert, zigzag, zorder, natural


curveMap = {
    "hilbert": hilbert.Hilbert,
    "zigzag": zigzag.ZigZag,
    "zorder": zorder.ZOrder,
    "natural": natural.Natural,
}
curves = curveMap.keys()


def fromSize(curve, dimension, size):
    """
        A convenience function for creating a specified curve by specifying
        size and dimension. All curves implement this common interface.
    """
    return curveMap[curve].fromSize(dimension, size)
