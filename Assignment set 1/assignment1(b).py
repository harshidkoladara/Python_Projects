from League import *

if __name__ == "__main__":
    # Add the games to League
    g1 = Game("Chess", 10)
    g2 = Game("Pocker", 20)
    g3 = Game("Monopoly", 40)

    # add the 5 teams to the League
    t1 = Team("Megamind")
    t2 = Team("X-man")
    t3 = Team("Eternals")
    t4 = Team("Avangers")
    t5 = Team("The Boys")

    # Team 1 played games and players
    p1 = Player("Megamind")
    p2 = Player("Metro Man")
    p3 = Player("Roxanne Ritchi")

    t1.add_player(p1)
    t1.add_player(p2)
    t1.add_player(p3)

    t1.game_played(g1, won=True)
    t1.game_played(g2, won= False)

    # adding team 2 players and played games
    p4 = Player('Wolverine')
    p5 = Player("Strome")
    p6 = Player("Magneto")
    p7 = Player("Proffessor-X")
    
    t2.add_player(p4)
    t2.add_player(p5)
    t2.add_player(p6)
    t2.add_player(p7)

    t2.game_played(g2, won=True)
    t2.game_played(g3, won=False)

    # adding team 3 players and played games
    p8 = Player("Sersi")
    p9 = Player("Druig")

    t3.add_player(p8)
    t3.add_player(p9)

    t3.game_played(g3, won=True)
    t3.game_played(g1, won=False)

    # adding Team 4 players and played games
    p10 = Player("Thanos")
    p11 = Player("Iron-man")
    p12 = Player("Thor")

    t4.add_player(p10)
    t4.add_player(p11)
    t4.add_player(p12)

    t4.game_played(g1, won=True)
    t4.game_played(g2, won=True)
    t4.game_played(g3, won=True)

    # adding team 5 players and played games
    p13 = Player("Billy Butcher")
    p14 = Player("Hughie Campbell")

    t5.add_player(p13)
    t5.add_player(p14)

    t5.game_played(g3, won=True)
    t5.game_played(g1, won=True)
    t5.game_played(g2, won=False)
    
    League.__str__()