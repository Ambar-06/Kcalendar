class ZoomClient:
    def __init__(self):
        pass

    def initialize_event(self, request, data, **kwargs):
        {
        "agenda": "My Meeting",
        "default_password": False,
        "duration": 60,
        "password": "",
        "pre_schedule": True,
        "schedule_for": kwargs.get("email"),
        "settings": {
            "additional_data_center_regions": [
            "TY"
            ],
            "allow_multiple_devices": True,
            "approval_type": 0,
            "approved_or_denied_countries_or_regions": {
            "approved_list": [
                "IN"
            ],
            "enable": True,
            "method": "approve"
            },
            "audio": "telephony",
            "audio_conference_info": "test",
            "authentication_domains": "example.com",
            "authentication_exception": [
            {
                "email": "jchill@example.com",
                "name": "Jill Chill"
            }
            ],
            "authentication_option": "signIn_D8cJuqWVQ623CI4Q8yQK0Q",
            "auto_recording": "cloud",
            "breakout_room": {
            "enable": true,
            "rooms": [
                {
                "name": "room1",
                "participants": [
                    "jchill@example.com"
                ]
                }
            ]
            },
            "calendar_type": 1,
            "close_registration": false,
            "contact_email": "jchill@example.com",
            "contact_name": "Jill Chill",
            "email_notification": true,
            "encryption_type": "enhanced_encryption",
            "focus_mode": true,
            "global_dial_in_countries": [
            "US"
            ],
            "host_video": true,
            "jbh_time": 0,
            "join_before_host": false,
            "language_interpretation": {
            "enable": true,
            "interpreters": [
                {
                "email": "interpreter@example.com",
                "languages": "US,FR"
                }
            ]
            },
            "sign_language_interpretation": {
            "enable": true,
            "interpreters": [
                {
                "email": "interpreter@example.com",
                "sign_language": "American"
                }
            ]
            },
            "meeting_authentication": true,
            "meeting_invitees": [
            {
                "email": "jchill@example.com"
            }
            ],
            "mute_upon_entry": false,
            "participant_video": false,
            "private_meeting": false,
            "registrants_confirmation_email": true,
            "registrants_email_notification": true,
            "registration_type": 1,
            "show_share_button": true,
            "use_pmi": false,
            "waiting_room": false,
            "watermark": false,
            "host_save_video_order": true,
            "alternative_host_update_polls": true,
            "internal_meeting": false,
            "continuous_meeting_chat": {
            "enable": true,
            "auto_add_invited_external_users": true
            },
            "participant_focused_meeting": false,
            "push_change_to_calendar": false,
            "resources": [
            {
                "resource_type": "whiteboard",
                "resource_id": "X4Hy02w3QUOdskKofgb9Jg",
                "permission_level": "editor"
            }
            ],
            "auto_start_meeting_summary": false,
            "auto_start_ai_companion_questions": false
        },
        "start_time": "2022-03-25T07:32:55Z",
        "template_id": "Dv4YdINdTk+Z5RToadh5ug==",
        "timezone": "America/Los_Angeles",
        "topic": "My Meeting",
        "tracking_fields": [
            {
            "field": "field1",
            "value": "value1"
            }
        ],
        "type": 2
        }