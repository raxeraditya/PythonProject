from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    @field_validator('username')
    def username_must_not_contain_spaces(cls, value):
        if ' ' in value:
            raise ValueError('Username must not contain spaces')
        return value
    
    @field_validator('password')
    def password_must_be_strong(cls, value):
        if len(value) < 3:
            raise ValueError('Password must be at least 8 characters long')
        return value
