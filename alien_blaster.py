# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Player(object):
    """Игрок в экшен-игре. """
    def blast(self, enemy):
        print("Игpoк стреляет во врага.\n")
        enemy.die()

    
class Alien(object):
    """ Враждебный пришелец-инопланетянин в зкшен-игре. """
    def die(self):
        print("Tяжeлo дыша. пришелец произносит: 'Ну, вот и все. Спета моя песенка.\n"
    "Уже и в глазах темнеет ... Передай полутора миллионам моих личинок. что я любил их\nПрощай. безжалостный мир")
    
# Основная часть программы
print("\t\tГибeль пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nHaжмитe Enter. чтобы выйти.")
