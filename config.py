class Config:
    # 🔹 Risk thresholds
    RISK_THRESHOLDS = {
        'LOW': 0.2,
        'MEDIUM': 0.5,
        'HIGH': 0.8
    }
    
    # 🔹 Risk threshold constants
    LOW_RISK_THRESHOLD = 0.2
    MEDIUM_RISK_THRESHOLD = 0.5
    HIGH_RISK_THRESHOLD = 0.8

    # 🔹 Weights (final score ke liye)
    LOCATION_WEIGHT = 0.25
    DEVICE_WEIGHT = 0.20
    BEHAVIOR_WEIGHT = 0.20
    NETWORK_WEIGHT = 0.15
    HISTORY_WEIGHT = 0.20

    # 🔹 GPS validation
    GPS_ACCURACY_THRESHOLD = 50   # 👈 IMPORTANT (error fix)
    MAX_SPEED = 120
    REALISTIC_SPEED = 120

    GPS_VALIDATION = {
        'latitude_tolerance': 0.01,
        'longitude_tolerance': 0.01,
        'valid_range': {
            'min_latitude': -90,
            'max_latitude': 90,
            'min_longitude': -180,
            'max_longitude': 180
        }
    }

    # 🔹 Claims history configuration
    CLAIMS_CONFIG = {
        'years_back': 5,
        'max_claim_amount': 100000,
        'required_documents': [
            'claim_form',
            'identity_proof',
            'location_proof'
        ]
    }
    
    # 🔹 Claims history storage (populated at runtime)
    CLAIMS_HISTORY = {}

    # 🔹 Fraud detection
    MAX_CLAIMS_PER_DAY = 5
    MAX_IP_SHARED_USERS = 3

    # 🔹 Decision mapping
    DECISION_MAP = {
        'LOW': 'INSTANT_PAYOUT',
        'MEDIUM': 'DELAYED_PAYOUT',
        'HIGH': 'MANUAL_REVIEW'
    }



# class Config:
#     RISK_THRESHOLDS = {
#         'low': 0.2,
#         'medium': 0.5,
#         'high': 0.8
#     }

#     WEIGHTS = {
#         'feature1': 0.3,
#         'feature2': 0.5,
#         'feature3': 0.2
#     }

#     GPS_VALIDATION = {
#         'latitude_tolerance': 0.01,
#         'longitude_tolerance': 0.01,
#         'valid_range': {
#             'min_latitude': -90,
#             'max_latitude': 90,
#             'min_longitude': -180,
#             'max_longitude': 180
#         }
#     }

#     CLAIMS_HISTORY = {
#         'years_back': 5,
#         'max_claim_amount': 100000,
#         'required_documents': ['claim_form', 'identity_proof', 'location_proof']
#     }