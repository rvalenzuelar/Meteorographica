# (C) British Crown Copyright 2017, Met Office
#
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#

# Functions for handling observations.

import version_2c

def fetch_observations(year,month=1,day=1,version='none'):
    """Get observations from the 20CR archive at NERSC.

    Data wil be stored locally in directory $SCRATCH/20CR, to be retrieved by :func:`load_observations`. If the local files that would be produced already exists, this function does nothing.

    For 20CR version 2c, the data is retrieved in calendar year blocks, and the 'month' and 'day' arguments are ignored. 

    Args:
        year (:obj:`int`): Year to get data for.
        month (:obj:`int`, optional): Month to get data for (1-12).
        day (:obj:`int`, optional): Day to get data for (1-31).
        version (:obj:`str`): 20CR version to retrieve data for.

    Raises:
        StandardError: If variable is not a supported value.
 
    |
    """

    if version=='2c':
        return version_2c.fetch_observations(year)
    raise StandardError("Unsupported version %s" % version)

def load_observations_1file(year,month,day,hour,version='none'):
    """Load observations from disc, that were used in the assimilation run at the time specified.

    Data must be available in directory $SCRATCH/20CR, previously retrieved by :func:`fetch_observations`.

    Args:
        year (:obj:`int`): Year of assimilation run.
        month (:obj:`int`): Month of assimilation run (1-12)
        day (:obj:`int`): Day of assimilation run (1-31).
        hour (:obj:`int`): Hour of assimilation run (0-23).
        version (:obj:`str`): 20CR version to load data from.

    Returns:
        :obj:`pandas.DataFrame`: Dataframe of observations.

    Raises:
        StandardError: Version number not supported, or data not on disc - see :func:`fetch_observations`

    |
    """

    if version=='2c':
        return version_2c.load_observations_1file(
                                 year,month,day,hour)
    raise StandardError("Unsupported version %s" % version)

def load_observations(start,end,version='none'):
    """Load observations from disc, for the selected period

    Data must be available in directory $SCRATCH/20CR, previously retrieved by :func:`fetch`.

    Args:
        start (:obj:`datetime.datetime`): Get observations at or after this time.
        end (:obj:`datetime.datetime`): Get observations before this time.
        version (:obj:`str`): 20CR version to load data from.

    Returns:
        :obj:`pandas.DataFrame`: Dataframe of observations.


    Raises:
        StandardError: Version number not supported, or data not on disc - see :func:`fetch_observations`

    |
    """

    if version=='2c':
        return version_2c.load_observations(start,end)
    raise StandardError("Unsupported version %s" % version)