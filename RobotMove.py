def RobotMove(moves):
    return moves.count("U") == moves.count("D") and moves.count("R")==moves.count("L")
    
   
moves = input("Enter moves in capital: like U,D,L,R: ")
print(RobotMove(moves))
    