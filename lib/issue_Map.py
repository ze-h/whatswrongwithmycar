
answer_effects = {
    #THIS IS AN EXAMPLE
    "q1": {
        0: {  # Corresponds to "Yes"
            "faulty_starter": 0.2,  # Increase the probability by 20%
            "bad_ignition_switch": 0.1  # Increase the probability by 10%
        },
        1: {  # Corresponds to "No"
            "dead_battery": 0.5  # Increase the probability by 50%
        }
    }

}

