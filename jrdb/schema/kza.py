schema = {
    "name": "kza",
    "type": "record",
    "fields": [
        {"start":   0, "end":   5, "type": "string", "name": "jockey_id"},
        {"start":   5, "end":   6, "type": "string", "name": "deleted_flag"},
        {"start":   6, "end":  14, "type": "string", "name": "deleted_yyyymmdd"},
        {"start":  14, "end":  26, "type": "string", "name": "name"},
        {"start":  26, "end":  56, "type": "string", "name": "name_kana"},
        {"start":  56, "end":  62, "type": "string", "name": "name_short"},
        {"start":  62, "end":  63, "type": "string", "name": "affiliation_id"},
        {"start":  63, "end":  67, "type": "string", "name": "affiliation_name"},
        {"start":  67, "end":  75, "type": "string", "name": "birthday"},
        {"start":  75, "end":  79, "type": "string", "name": "license_year"},
        {"start":  79, "end":  80, "type": "string", "name": "apprentice_id"},
        {"start":  80, "end":  85, "type": "string", "name": "stable_trainer_id"},
        {"start":  85, "end": 125, "type": "string", "name": "comment"},
        {"start": 125, "end": 133, "type": "string", "name": "comment_yyyymmdd"},
        {"start": 133, "end": 136, "type": "string", "name": "leading_in_this_year"},
        {"start": 136, "end": 148, "type": "string", "name": "flat_race_in_this_year"},
        {"start": 148, "end": 160, "type": "string", "name": "steeplechase_race_in_this_year"},
        {"start": 160, "end": 163, "type": "string", "name": "win_grade_race_in_this_year"},
        {"start": 163, "end": 166, "type": "string", "name": "win_grade_race_in_this_year"},
        {"start": 166, "end": 169, "type": "string", "name": "leading_in_last_year"},
        {"start": 169, "end": 181, "type": "string", "name": "flat_race_in_last_year"},
        {"start": 181, "end": 193, "type": "string", "name": "steeplechase_race_in_last_year"},
        {"start": 193, "end": 196, "type": "string", "name": "win_stakes_race_in_last_year"},
        {"start": 196, "end": 199, "type": "string", "name": "win_grade_race_in_last_year"},
        {"start": 199, "end": 219, "type": "string", "name": "flat_race_in_total"},
        {"start": 219, "end": 239, "type": "string", "name": "steeplechase_race_in_total"},
        {"start": 239, "end": 247, "type": "string", "name": "data_yyyymmdd"}
    ]
}
