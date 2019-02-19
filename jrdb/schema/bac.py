schema = {
    "name": "bac",
    "type": "record",
    "fields": [
        {"start":   0, "end":   2, "type": "string", "name": "place_id"},
        {"start":   2, "end":   4, "type": "string", "name": "year"},
        {"start":   4, "end":   5, "type": "string", "name": "kai"},
        {"start":   5, "end":   6, "type": "string", "name": "nichi"},
        {"start":   6, "end":   8, "type": "string", "name": "number_of_race"},
        {"start":   8, "end":  16, "type": "string", "name": "yyyymmdd"},
        {"start":  16, "end":  20, "type": "string", "name": "start_at"},
        {"start":  20, "end":  24, "type": "string", "name": "distance"},
        {"start":  24, "end":  25, "type": "string", "name": "track_type_id"},
        {"start":  25, "end":  26, "type": "string", "name": "track_rotation_id"},
        {"start":  26, "end":  27, "type": "string", "name": "track_uchisoto_id"},
        {"start":  27, "end":  29, "type": "string", "name": "race_type_id"},
        {"start":  29, "end":  31, "type": "string", "name": "race_class_id"},
        {"start":  31, "end":  34, "type": "string", "name": "race_mark_id"},
        {"start":  34, "end":  35, "type": "string", "name": "race_weight_id"},
        {"start":  35, "end":  36, "type": "string", "name": "race_grade"},
        {"start":  36, "end":  86, "type": "string", "name": "race_name"},
        {"start":  86, "end":  94, "type": "string", "name": "race_times"},
        {"start":  94, "end":  96, "type": "string", "name": "number_of_horse"},
        {"start":  96, "end":  97, "type": "string", "name": "course_id"},
        {"start":  97, "end":  98, "type": "string", "name": "locale_id"},
        {"start":  98, "end": 106, "type": "string", "name": "race_name_short"},
        {"start": 106, "end": 124, "type": "string", "name": "race_name_9chars"},
        {"start": 124, "end": 125, "type": "string", "name": "bac_data_id"},
        {"start": 125, "end": 130, "type": "string", "name": "prize_1st"},
        {"start": 130, "end": 135, "type": "string", "name": "prize_2nd"},
        {"start": 135, "end": 140, "type": "string", "name": "prize_3rd"},
        {"start": 140, "end": 145, "type": "string", "name": "prize_4th"},
        {"start": 145, "end": 150, "type": "string", "name": "prize_5th"},
        {"start": 150, "end": 155, "type": "string", "name": "earnings_1st"},
        {"start": 155, "end": 160, "type": "string", "name": "earnings_2nd"},
        {"start": 160, "end": 176, "type": "string", "name": "betting_ticket_sale_flag"},
        {"start": 176, "end": 177, "type": "string", "name": "win5_flag"}
    ]
}