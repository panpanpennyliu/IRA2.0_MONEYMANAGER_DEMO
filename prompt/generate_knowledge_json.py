GENERATE_BUSINESS_FLOW_REQUEST = """
Based on each frame's state transitions and action description, to summerize business process steps and structure them in a "business_flow" JSON attribute, where the step index (like 'step 1') serves as the key and the step description as the value. For reporting click operations, describe with the description of the UI element instead of position coordinates. Exclude any step not present in the frame; do not include any redundant details. In the business flow, merge sequences of steps involving pressing a command key down, acting and then releasing the command key into one step. For example, if the step sequences are as follows: 1. Press and hold the Ctrl key, 2. Press the 'C' key, 3. Release the Ctrl key. Then these steps should be merged into a single step: 1. Press Ctrl+C.
"""

EXTRACT_STEP_DESC_STATE_TRANS = """
Keep only the part of the JSON data where the attribute is "action_description" and "state_transition_caption", and remove all the other parts.
"""

COMPILE_KNOWLEDGE_JSON_REQUEST="""
Merge the JSON date for each frame into a single JSON array named 'framesInfo' as the output. Keep attributes of diffrent frames separate. Place each frame's attributes directly under 'framesInfo', without any intermediate field. Then merge 'framesInfo' and 'business_flow' into a single JSON object named 'knowledgeJson' as the output.
"""

