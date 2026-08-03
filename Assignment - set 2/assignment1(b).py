from League import *

if __name__ == "__main__":
    # Add the games to League
    g1 = Game("Tennis", 40)
    g2 = Game("Table Tennis", 90)
    g3 = Game("Relly Race", 100)

    # add the 5 teams to the League
    t1 = Team("A")
    t2 = Team("B")
    t3 = Team("C")
    t4 = Team("D")
    t5 = Team("E")

    # Team 1 played games and players
    p1 = Player("A1")
    p2 = Player("A2")
    p3 = Player("A3")

    t1.add_player(p1)
    t1.add_player(p2)
    t1.add_player(p3)

    t1.game_played(g1, won=True)
    t1.game_played(g2, won= False)

    # adding team 2 players and played games
    p4 = Player('B1')
    p5 = Player("B2")
    p6 = Player("B3")
    p7 = Player("B4")
    
    t2.add_player(p4)
    t2.add_player(p5)
    t2.add_player(p6)
    t2.add_player(p7)

    t2.game_played(g2, won=True)
    t2.game_played(g3, won=False)

    # adding team 3 players and played games
    p8 = Player("C1")
    p9 = Player("C2")

    t3.add_player(p8)
    t3.add_player(p9)

    t3.game_played(g3, won=True)
    t3.game_played(g1, won=False)

    # adding Team 4 players and played games
    p10 = Player("D1")
    p11 = Player("D2")
    p12 = Player("D3")

    t4.add_player(p10)
    t4.add_player(p11)
    t4.add_player(p12)

    t4.game_played(g1, won=True)
    t4.game_played(g2, won=True)
    t4.game_played(g3, won=True)

    # adding team 5 players and played games
    p13 = Player("E1")
    p14 = Player("E2")

    t5.add_player(p13)
    t5.add_player(p14)

    t5.game_played(g3, won=True)
    t5.game_played(g1, won=True)
    t5.game_played(g2, won=False)
    
    League.__str__()