from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(String(10), nullable=False)
    character_favorites: Mapped["Favorites"] = relationship(back_populates = "favorites_characters")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
        }
    
class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(String(100000000000), nullable=False)
    planet_favorites: Mapped["Favorites"] = relationship(back_populates = "favorites_planets")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population
        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey=("Characters.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey=("Planets.id"))
    favorites_characters: Mapped[list["Characters"]] = relationship(back_populates = "character_favorites")
    favorites_planets: Mapped[list["Planets"]] = relationship(back_populates = "planet_favorites")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
        }