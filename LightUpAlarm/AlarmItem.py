#!/usr/bin/env python2
#
# Class to define an Alarm.
#
# Copyright (c) 2015 carlosperate https://github.com/carlosperate/
# Licensed under The MIT License (MIT), a copy can be found in the LICENSE file
#
# Full description goes here
#
from __future__ import unicode_literals, absolute_import, print_function
from __builtin__ import property
import collections
import types
import sys


class AlarmItem(object):
    """
    .
    """
    #
    # metaclass methods: constructor and print
    #
    def __init__(self, hour, minute,
                 days=(False, False, False, False, False, False, False),
                 enabled=True, alarm_id=None):
        """
        Constructor assigns the input data into the new alarm instance.
        First creates the private variables, then assigns values
        """
        # ID is only created at first save into db
        self.__id = None
        # Indicates if the alarm is enabled or not
        self.__enabled = False
        # Alarm time
        self.__minute = 0
        self.__hour = 0
        # Contains the days of the weeks that this alarm repeats
        self.__repeat = collections.OrderedDict()
        self.__repeat['Monday'] = False
        self.__repeat['Tuesday'] = False
        self.__repeat['Wednesday'] = False
        self.__repeat['Thursday'] = False
        self.__repeat['Friday'] = False
        self.__repeat['Saturday'] = False
        self.__repeat['Sunday'] = False

        # Assigning values using accessors
        self.hour = hour
        self.minute = minute
        self.repeat = days
        self.enabled = enabled
        if alarm_id is not None:
            self.id_ = alarm_id

    def __str__(self):
        """
        Converts the class instance data into a readable string format.
        :return: String with all the alarm data.
        """
        ret_str = 'Alarm ID: %3d | Time: %02d:%02d | Enabled: %5s | Repeat: ' %\
                  (self.id_, self.hour, self.minute, self.enabled)
        for day in self.__repeat:
            if self.__repeat[day] is True:
                ret_str += "%s " % str(day)[:3]
            else:
                ret_str += "--- "

        return ret_str

    #
    # id accesor
    #
    def __get_id(self):
        return self.__id

    def __set_id(self, new_id):
        """
        Sets id value. Must be an integer.
        :param new_id: new ID for the alarm instance.
        """
        if isinstance(new_id, types.IntType):
            self.__id = new_id
        else:
            print('ERROR: Provided AlarmItem().id type is not an Integer' +
                  ': %s!' % new_id, file=sys.stderr)

    id_ = property(__get_id, __set_id)

    #
    # enabled accesor
    #
    def __get_enabled(self):
        return self.__enabled

    def __set_enabled(self, new_enabled):
        """
        Ensure new value is a boolean before setting the enabled state.
        :param new_enabled: new enabled state for the alarm instance.
        """
        if isinstance(new_enabled, types.BooleanType):
            self.__enabled = new_enabled
        else:
            print('ERROR: Provided AlarmItem().enabled type is not a boolean' +
                  ': %s!' % new_enabled, file=sys.stderr)

    enabled = property(__get_enabled, __set_enabled)

    #
    # minute accesor
    #
    def __get_minute(self):
        return self.__minute

    def __set_minute(self, new_minute):
        """
        Checks input is an integer and wraps around value to be between 0 - 59.
        :param new_minute: new alarm minutes for the alarm instance.
        """
        if isinstance(new_minute, types.IntType):
            while new_minute >= 60:
                new_minute %= 60
            self.__minute = new_minute
        else:
            print('ERROR: Provided AlarmItem().minute type is not an Integer' +
                  ': %s!' % new_minute, file=sys.stderr)

    minute = property(__get_minute, __set_minute)

    #
    # hour accesor
    #
    def __get_hour(self):
        return self.__hour

    def __set_hour(self, new_hour):
        """
        Checks input is an integer and wraps around value to be between 0 - 23.
        :param new_hour: new alarm hours for the alarm instance.
        """
        if isinstance(new_hour, types.IntType):
            while new_hour >= 24:
                new_hour %= 24
            self.__hour = new_hour
        else:
            print('ERROR: Provided AlarmItem().hour type is not an Integer' +
                  ': %s!' % new_hour, file=sys.stderr)

    hour = property(__get_hour, __set_hour)

    #
    # repeat accesor
    #
    def __get_repeat(self):
        """
        Returns the days of the week alarm repetition in the form of a tuple.
        :return: Tuple with 7 booleans to indicate repetition for the weekdays.
        """
        repeat_tuple = (self.__repeat['Monday'], self.__repeat['Tuesday'],
                        self.__repeat['Wednesday'], self.__repeat['Thursday'],
                        self.__repeat['Friday'], self.__repeat['Saturday'],
                        self.__repeat['Sunday'])
        return repeat_tuple

    def __set_repeat(self, new_repeat):
        """
        Checks that it is a list/tuple of 7 booleans and if so assigns them to
        the _repeat dictionary.
        :param new_repeat: List of containing 7 booleans to indicate the days
                           of the week the alarm repeats.
        """
        if len(new_repeat) == 7:
            for day in new_repeat:
                if not isinstance(day, types.BooleanType):
                    print('ERROR: All items in the AlarmItem().repeat list ' +
                          'have to be Booleans!', file=sys.stderr)
                    break
            else:
                day_int = 0
                for day in self.__repeat:
                    self.__repeat[day] = new_repeat[day_int]
                    day_int += 1
        else:
            print('ERROR: The AlarmItem().repeat must be a list of 7 booleans!',
                  file=sys.stderr)

    repeat = property(__get_repeat, __set_repeat)

    def __get_monday(self):
        return self.__repeat['Monday']

    def __set_monday(self, new_monday):
        if isinstance(new_monday, types.BooleanType):
            self.__repeat['Monday'] = new_monday
        else:
            print('ERROR: New value for the AlarmItem().monday variable has ' +
                  'to be a Boolean !', file=sys.stderr)

    monday = property(__get_monday, __set_monday)

    def __get_tuesday(self):
        return self.__repeat['Tuesday']

    def __set_tuesday(self, new_tuesday):
        if isinstance(new_tuesday, types.BooleanType):
            self.__repeat['Tuesday'] = new_tuesday
        else:
            print('ERROR: New value for the AlarmItem().tuesday variable has ' +
                  'to be a Boolean !', file=sys.stderr)

    tuesday = property(__get_tuesday, __set_tuesday)

    def __get_wednesday(self):
        return self.__repeat['Wednesday']

    def __set_wednesday(self, new_wednesday):
        if isinstance(new_wednesday, types.BooleanType):
            self.__repeat['Wednesday'] = new_wednesday
        else:
            print('ERROR: New value for the AlarmItem().wednesday variable ' +
                  'has to be a Boolean !', file=sys.stderr)

    wednesday = property(__get_wednesday, __set_wednesday)

    def __get_thursday(self):
        return self.__repeat['Thursday']

    def __set_thursday(self, new_thursday):
        if isinstance(new_thursday, types.BooleanType):
            self.__repeat['Thursday'] = new_thursday
        else:
            print('ERROR: New value for the AlarmItem().thursday variable ' +
                  'has to be a Boolean !', file=sys.stderr)

    thursday = property(__get_thursday, __set_thursday)

    def __get_friday(self):
        return self.__repeat['Friday']

    def __set_friday(self, new_friday):
        if isinstance(new_friday, types.BooleanType):
            self.__repeat['Friday'] = new_friday
        else:
            print('ERROR: New value for the AlarmItem().friday variable has ' +
                  'to be a Boolean !', file=sys.stderr)

    friday = property(__get_friday, __set_friday)

    def __get_saturday(self):
        return self.__repeat['Saturday']

    def __set_saturday(self, new_saturday):
        if isinstance(new_saturday, types.BooleanType):
            self.__repeat['Saturday'] = new_saturday
        else:
            print('ERROR: New value for the AlarmItem().saturday variable ' +
                  'has to be a Boolean !', file=sys.stderr)

    saturday = property(__get_saturday, __set_saturday)

    def __get_sunday(self):
        return self.__repeat['Sunday']

    def __set_sunday(self, new_sunday):
        if isinstance(new_sunday, types.BooleanType):
            self.__repeat['Sunday'] = new_sunday
        else:
            print('ERROR: New value for the AlarmItem().sunday variable ' +
                  'has to be a Boolean !', file=sys.stderr)

    sunday = property(__get_sunday, __set_sunday)

    #
    # member methods to retrieve specific data
    #
    def any_enabled_day(self):
        """
        Check if there are any repeat days enabled.
        :return: A boolean value indicating if an repeat weekday is activated.
        """
        any_enabled = False
        for day in self.__repeat:
            if self.__repeat[day] is True:
                any_enabled = True
        return any_enabled

    #
    # member methods to calculate time
    #
    def minutes_to_alert(self, hour, minute, weekday):
        """
        Calculates the time in minutes that will elapse from the initial
        reference input time and weekday and the first time this alarm will have
        to trigger an alert (independently of this alarm being active or not).
        :param hour: start hour, value 0-23.
        :param minute: start minute, value 0-59.
        :param weekday: start weekday, value 0-6.
        :return: Integer indicating the amount in minutes until the alarm
                 triggers from the initial reference time and weekday.
        """
        alarm_day_minute = self.minute + (self.hour * 60)
        ref_day_minute = minute + (hour * 60)
        one_day_minutes = 1440

        # First corner case, check the same day after input time
        if (self.repeat[weekday] is True) and \
                (alarm_day_minute >= ref_day_minute):
            return alarm_day_minute - ref_day_minute

        # Check the rest of the week until, but not including, the same day
        day = weekday + 1
        if day > 6:
            day = 0
        day_count = 1
        while day != weekday:
            if self.repeat[day] is True:
                # Add the days in minutes and relative time to reference
                minutes_difference = day_count * one_day_minutes
                if alarm_day_minute >= ref_day_minute:
                    minutes_difference += alarm_day_minute - ref_day_minute
                else:
                    minutes_difference -= ref_day_minute - alarm_day_minute
                # Returns on first encountered alarm
                return minutes_difference
            else:
                day += 1
                day_count += 1
                if day > 6:
                    day = 0

        # Second corner case, check the same day before input time
        if (self.repeat[weekday] is True) and \
                (ref_day_minute > alarm_day_minute):
            return (one_day_minutes * 7) - ref_day_minute + alarm_day_minute

        # Alarm has no enabled days
        return None
