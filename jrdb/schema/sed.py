schema = {
    "name": "sed",
    "type": "record",
    "fields": [
        {"start":   0, "end":   2, "type": "string", "name": "place_id"},
        {"start":   2, "end":   4, "type": "string", "name": "year"},
        {"start":   4, "end":   5, "type": "string", "name": "kai"},
        {"start":   5, "end":   6, "type": "string", "name": "nichi"},
        {"start":   6, "end":   8, "type": "string", "name": "number_of_race"},
        {"start":   8, "end":  10, "type": "string", "name": "pp"},
        {"start":  10, "end":  18, "type": "string", "name": "horse_id"},
        {"start":  18, "end":  26, "type": "string", "name": "yyyymmdd"},
        {"start":  26, "end":  62, "type": "string", "name": "horse_name"},
        {"start":  62, "end":  66, "type": "string", "name": "distance"},
        {"start":  66, "end":  67, "type": "string", "name": "track_type_id"},
        {"start":  67, "end":  68, "type": "string", "name": "track_rotation_id"},
        {"start":  68, "end":  69, "type": "string", "name": "track_uchisoto_id"},
        {"start":  69, "end":  71, "type": "string", "name": "track_cond_id"},
        {"start":  71, "end":  73, "type": "string", "name": "race_type_id"},
        {"start":  73, "end":  75, "type": "string", "name": "race_class_id"},
        {"start":  75, "end":  78, "type": "string", "name": "race_mark_id"},
        {"start":  78, "end":  79, "type": "string", "name": "race_weight_id"},
        {"start":  79, "end":  80, "type": "string", "name": "race_grade"},
        {"start":  80, "end": 130, "type": "string", "name": "race_name"},
        {"start": 130, "end": 132, "type": "string", "name": "number_of_horse"},
        {"start": 132, "end": 140, "type": "string", "name": "race_name_short"},
        {"start": 140, "end": 142, "type": "string", "name": "fp"},
        {"start": 142, "end": 143, "type": "string", "name": "exception_id"},
        {"start": 143, "end": 147, "type": "string", "name": "finish_time"},
        {"start": 147, "end": 150, "type": "string", "name": "jockey_weight"},
        {"start": 150, "end": 162, "type": "string", "name": "jockey_name"},
        {"start": 162, "end": 174, "type": "string", "name": "trainer_name"},
        {"start": 174, "end": 180, "type": "string", "name": "win_odds"},
        {"start": 180, "end": 182, "type": "string", "name": "win_fav_rank"},
        {"start": 182, "end": 185, "type": "string", "name": "idm"},
        {"start": 185, "end": 188, "type": "string", "name": "base_score"},
        {"start": 188, "end": 191, "type": "string", "name": "cond_spped_score"},
        {"start": 191, "end": 194, "type": "string", "name": "pace_score"},
        {"start": 194, "end": 197, "type": "string", "name": "delay_score"},
        {"start": 197, "end": 200, "type": "string", "name": "positioning_score"},
        {"start": 200, "end": 203, "type": "string", "name": "disadvantage_score"},
        {"start": 203, "end": 206, "type": "string", "name": "disadvantage_score1"},
        {"start": 206, "end": 209, "type": "string", "name": "disadvantage_score2"},
        {"start": 209, "end": 212, "type": "string", "name": "disadvantage_score3"},
        {"start": 212, "end": 215, "type": "string", "name": "race_score"},
        {"start": 215, "end": 216, "type": "string", "name": "racing_line_id"},
        {"start": 216, "end": 217, "type": "string", "name": "horse_cond_id"},
        {"start": 217, "end": 219, "type": "string", "name": "horse_ability_id"},
        {"start": 219, "end": 220, "type": "string", "name": "body_type_id"},
        {"start": 220, "end": 221, "type": "string", "name": "horse_fitness_id"},
        {"start": 221, "end": 222, "type": "string", "name": "race_pace"},
        {"start": 222, "end": 223, "type": "string", "name": "horse_pace"},
        {"start": 223, "end": 228, "type": "string", "name": "ten_score"},
        {"start": 228, "end": 233, "type": "string", "name": "agari_score"},
        {"start": 233, "end": 238, "type": "string", "name": "horse_pace_score"},
        {"start": 238, "end": 243, "type": "string", "name": "race_pace_score"},
        {"start": 243, "end": 255, "type": "string", "name": "horse_name_1st"},
        {"start": 255, "end": 258, "type": "string", "name": "time_diff_1st"},
        {"start": 258, "end": 261, "type": "string", "name": "f3f_time"},
        {"start": 261, "end": 264, "type": "string", "name": "l3f_time"},
        {"start": 264, "end": 288, "type": "string", "name": "memo"},
        {"start": 290, "end": 296, "type": "string", "name": "show_odds_under"},
        {"start": 296, "end": 302, "type": "string", "name": "win_odds_at_10am"},
        {"start": 302, "end": 308, "type": "string", "name": "show_odds_at_10am"},
        {"start": 308, "end": 310, "type": "string", "name": "corner1_pos"},
        {"start": 310, "end": 312, "type": "string", "name": "corner2_pos"},
        {"start": 312, "end": 314, "type": "string", "name": "corner3_pos"},
        {"start": 314, "end": 316, "type": "string", "name": "corner4_pos"},
        {"start": 316, "end": 319, "type": "string", "name": "time_diff_f3f"},
        {"start": 319, "end": 322, "type": "string", "name": "time_diff_l3f"},
        {"start": 322, "end": 327, "type": "string", "name": "jockey_id"},
        {"start": 327, "end": 332, "type": "string", "name": "trainer_id"},
        {"start": 332, "end": 335, "type": "string", "name": "horse_weight"},
        {"start": 335, "end": 338, "type": "string", "name": "horse_weight_diff"},
        {"start": 338, "end": 339, "type": "string", "name": "weather_id"},
        {"start": 339, "end": 340, "type": "string", "name": "course_id"},
        {"start": 340, "end": 341, "type": "string", "name": "running_strategy_id"},
        {"start": 341, "end": 348, "type": "string", "name": "win_payoff"},
        {"start": 348, "end": 355, "type": "string", "name": "show_payoff"},
        {"start": 355, "end": 360, "type": "string", "name": "prize"},
        {"start": 360, "end": 365, "type": "string", "name": "earnings"},
        {"start": 365, "end": 367, "type": "string", "name": "race_pace_flow_id"},
        {"start": 367, "end": 369, "type": "string", "name": "horse_pace_flow_id"},
        {"start": 369, "end": 370, "type": "string", "name": "corner4_racing_line_id"}
    ]
}
