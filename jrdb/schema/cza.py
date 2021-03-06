schema = {
    "name": "cza",
    "type": "record",
    "fields": [
        {"start":   0, "end":   5, "type": "string", "name": "trainer_id"},
        {"start":   5, "end":   6, "type": "string", "name": "deleted_flag"},
        {"start":   6, "end":  14, "type": "string", "name": "deleted_yyyymmdd"},
        {"start":  14, "end":  26, "type": "string", "name": "name"},
        {"start":  26, "end":  56, "type": "string", "name": "name_kana"},
        {"start":  56, "end":  62, "type": "string", "name": "name_short"},
        {"start":  62, "end":  63, "type": "string", "name": "affiliation_id"},
        {"start":  63, "end":  67, "type": "string", "name": "affiliation_name"},
        {"start":  67, "end":  75, "type": "string", "name": "birthday"},
        {"start":  75, "end":  79, "type": "string", "name": "license_year"},
        {"start":  79, "end": 119, "type": "string", "name": "comment"},
        {"start": 119, "end": 127, "type": "string", "name": "comment_yyyymmdd"},
        {"start": 127, "end": 130, "type": "string", "name": "leading_in_this_year"},
        {"start": 130, "end": 142, "type": "string", "name": "flat_race_in_this_year"},
        {"start": 142, "end": 154, "type": "string", "name": "steeplechase_race_in_this_year"},
        {"start": 154, "end": 157, "type": "string", "name": "win_stakes_race_in_this_year"},
        {"start": 157, "end": 160, "type": "string", "name": "win_grade_race_in_this_year"},
        {"start": 160, "end": 163, "type": "string", "name": "leading_in_last_year"},
        {"start": 163, "end": 175, "type": "string", "name": "flat_race_in_last_year"},
        {"start": 175, "end": 187, "type": "string", "name": "steeplechase_race_in_last_year"},
        {"start": 187, "end": 190, "type": "string", "name": "win_stakes_race_in_last_year"},
        {"start": 190, "end": 193, "type": "string", "name": "win_grade_race_in_last_year"},
        {"start": 193, "end": 213, "type": "string", "name": "flat_race_in_total"},
        {"start": 213, "end": 233, "type": "string", "name": "steeplechase_race_in_total"},
        {"start": 233, "end": 241, "type": "string", "name": "data_yyyymmdd"}
    ]
}
