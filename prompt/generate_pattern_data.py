GENERATE_UNIQUE_ID_REQUEST= """
Create two new JSON attributes "unique_id" and "behavior_id", both set value with '{id}', and append them to the frame JSON data, then output in JSON format.
"""

MERGE_BEHAVIOR_ID_REQUEST= """
Based on frames JSON data, to merge frames with identical "user_action" and "dance_caption" information across different videos. Given frames from multiple videos identified by "video_id", compare "user_action" and "dance_caption" information in each frame. When two frames from different videos share the same action and dance caption:
1. Standardize their "behavior_id", adopting the lower of the two original "behavior_id".
2. Use "video_id" to distinguish frames from different videos.
"""