from datetime import datetime
from typing import Union

from pydantic import BaseModel, validator, Field


class DepositModel(BaseModel):
    date: str = Field(
        title="Date of application", description="dd.mm.YYYY", default="01.01.2023"
    )
    periods: int = Field(
        title="Number of months on deposit", description="1-60", default=3
    )
    amount: int = Field(
        title="Deposit amount", description="10 000-3 000 000", default=10000
    )
    rate: float = Field(title="Deposit interest", description="1-8", default=1.5)

    @validator("date", pre=True)
    def validate_date_format(cls, v) -> str:
        try:
            datetime.strptime(v, "%d.%m.%Y")
            return v
        except ValueError:
            raise ValueError("should be a string in the format 'dd.mm.YYYY'")

    @validator("periods", pre=True)
    def validate_periods(cls, value) -> int:
        if not isinstance(value, int) or not (1 <= value <= 60):
            raise ValueError(
                "invalid value for 'periods'. Should be an integer between 1 and 60"
            )
        return value

    @validator("amount", pre=True)
    def validate_amount(cls, value) -> int:
        if not isinstance(value, int) or not (10000 <= value <= 3000000):
            raise ValueError("should be an integer between 10000 and 3000000")
        return value

    @validator("rate", pre=True)
    def validate_rate(cls, value) -> Union[float, int]:
        if not isinstance(value, (float, int)) or not (1 <= value <= 8):
            raise ValueError("should be a float between 1 and 8")
        return value
