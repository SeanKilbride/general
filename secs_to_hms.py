def secs_to_hms(secs):
    hours_full = secs // 3600     # full hours
    hours_rem  = secs % 3600      # hours remainder 
    mins_full  = hours_rem // 60  # full mins
    secs   = hours_rem % 60   # mins remainder i.e. secs
    return [hours_full, mins_full, secs]

for i in [60, 5.5*60, 7.25*60, 0.5*3600, 2.25*3600, 2.25*3600+60]:
    h_m_s_list = secs_to_hms(i)
    print(i, "seconds =     ", h_m_s_list[0], ":", h_m_s_list[1], ":", h_m_s_list[2] , " hh:mm:ss" )
    


