#!/usr/bin/env python
def drop_first_last(name,email,*phone):
    print phone
record=["sameer","s@email.com",'22344','4444','4444224']
#drop_first_last("sameer","gawande@yahoo.com","408-306-6372","202-736-7814","565331")
drop_first_last(*record)
