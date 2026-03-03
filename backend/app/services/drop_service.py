import random
from app.database import SessionLocal
from app.models.character import Character
from app.models.inventory import Inventory
from app.models.user import User

RARITY_CHANCES = {
    "Common": 60,
    "Rare": 25,
    "Epic": 10,
    "Legendary": 4,
    "Celestial": 1
}

def choose_rarity():
    roll = random.randint(1, 100)
    cumulative = 0

    for rarity, chance in RARITY_CHANCES.items():
        cumulative += chance
        if roll <= cumulative:
            return rarity

def drop_character(telegram_id: int):
    db = SessionLocal()

    user = db.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        db.close()
        return None

    rarity = choose_rarity()

    # Celestial uniqueness check
    if rarity == "Celestial":
        existing = db.query(Character).filter_by(rarity="Celestial").first()
        if existing:
            rarity = "Legendary"

    characters = db.query(Character).filter_by(rarity=rarity).all()

    if not characters:
        db.close()
        return None

    character = random.choice(characters)

    inventory_item = db.query(Inventory).filter_by(
        user_id=user.id,
        character_id=character.id
    ).first()

    if inventory_item:
        inventory_item.quantity += 1
    else:
        inventory_item = Inventory(
            user_id=user.id,
            character_id=character.id,
            quantity=1
        )
        db.add(inventory_item)

    db.commit()
    db.close()

    return character
