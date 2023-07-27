import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate_deposit():
    payload = {"date": "31.01.2023", "periods": 60, "amount": 3000000, "rate": 5}

    expected_response = {
        "31.01.2023": 3012500,
        "28.02.2023": 3025052.08,
        "31.03.2023": 3037656.47,
        "30.04.2023": 3050313.37,
        "31.05.2023": 3063023.01,
        "30.06.2023": 3075785.6,
        "31.07.2023": 3088601.38,
        "31.08.2023": 3101470.55,
        "30.09.2023": 3114393.34,
        "31.10.2023": 3127369.98,
        "30.11.2023": 3140400.69,
        "31.12.2023": 3153485.69,
        "31.01.2024": 3166625.22,
        "29.02.2024": 3179819.49,
        "31.03.2024": 3193068.74,
        "30.04.2024": 3206373.19,
        "31.05.2024": 3219733.08,
        "30.06.2024": 3233148.63,
        "31.07.2024": 3246620.09,
        "31.08.2024": 3260147.67,
        "30.09.2024": 3273731.62,
        "31.10.2024": 3287372.17,
        "30.11.2024": 3301069.55,
        "31.12.2024": 3314824.01,
        "31.01.2025": 3328635.77,
        "28.02.2025": 3342505.09,
        "31.03.2025": 3356432.19,
        "30.04.2025": 3370417.33,
        "31.05.2025": 3384460.73,
        "30.06.2025": 3398562.65,
        "31.07.2025": 3412723.33,
        "31.08.2025": 3426943.01,
        "30.09.2025": 3441221.94,
        "31.10.2025": 3455560.37,
        "30.11.2025": 3469958.53,
        "31.12.2025": 3484416.69,
        "31.01.2026": 3498935.1,
        "28.02.2026": 3513513.99,
        "31.03.2026": 3528153.63,
        "30.04.2026": 3542854.27,
        "31.05.2026": 3557616.17,
        "30.06.2026": 3572439.57,
        "31.07.2026": 3587324.73,
        "31.08.2026": 3602271.92,
        "30.09.2026": 3617281.39,
        "31.10.2026": 3632353.39,
        "30.11.2026": 3647488.2,
        "31.12.2026": 3662686.07,
        "31.01.2027": 3677947.26,
        "28.02.2027": 3693272.04,
        "31.03.2027": 3708660.67,
        "30.04.2027": 3724113.42,
        "31.05.2027": 3739630.56,
        "30.06.2027": 3755212.36,
        "31.07.2027": 3770859.07,
        "31.08.2027": 3786570.99,
        "30.09.2027": 3802348.37,
        "31.10.2027": 3818191.49,
        "30.11.2027": 3834100.62,
        "31.12.2027": 3850076.04,
    }

    response = client.post("/api/v1/deposit/calculate", json=payload)

    assert response.status_code == 200

    assert isinstance(response.json(), dict)

    assert response.json() == expected_response
