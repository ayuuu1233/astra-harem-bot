from app.database import SessionLocal
from app.models.user import User
from app.models.inventory import Inventory
from app.models.character import Character

RARITY_VALUES = {
    "Common": 10,
    "Rare": 30,
    "Epic": 75,
    "Legendary": 200,
    "Celestial": 1000
}

def sell_character(telegram_id: int, character_name: str):
    db = SessionLocal()

    user = db.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        db.close()
        return None, "User not found."

    character = db.query(Character).filter_by(name=character_name).first()
    if not character:
        db.close()
        return None, "Character not found."

    inventory_item = db.query(Inventory).filter_by(
        user_id=user.id,
        character_id=character.id
    ).first()

    if not inventory_item or inventory_item.quantity <= 0:
        db.close()
        return None, "You don't own this character."

    value = RARITY_VALUES.get(character.rarity, 5)

    inventory_item.quantity -= 1
    user.coins += value

    db.commit()
    db.close()

    return value, None
