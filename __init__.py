# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Orthogonalize
                                 A QGIS plugin
 Orthogonalize selected object
                             -------------------
        begin                : 2016-05-27
        copyright            : (C) 2016 by Dkrav/GeoInfoCenter
        email                : dkrav2006@yandex.ua
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Orthogonalize class from file Orthogonalize.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .orthoganalizer import Orthogonalize
    return Orthogonalize(iface)
