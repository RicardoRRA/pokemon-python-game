import random


class Pokemon:  # <-- Por padrão classes começãm com a letra maiuscula exemplo: PokemonDeFogo

    def __init__(self, especie, level=None, nome=None):  # <-- metodo __init__ é chamando de construtor, com ele vc "constroi as coisas"
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo

        print("{} perdeu {} pontos de vida".format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado".format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabrça de {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lançou um jato de água em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonPM(Pokemon):
    tipo = "miliciano"

    def atacar(self, pokemon):
        print("{} lançou um jato de spray de pimenta em {}".format(self, pokemon))
        return super().atacar(pokemon)

