from models.games.quizz import Quizz


class BattleRoyal(Quizz):

    def __init__(self, channel, creator_id, category) -> None:
        super().__init__(channel, creator_id, category)
        

    def _compute_score(self):

        for player in self.players:
            player_answer = [pa[1] for pa in self.player_answer if pa[0] == player]
            if not player_answer or  not self.current_question.check_answer(player_answer[0]):
                player.loose_life_point()

        players_in_life = [p for p in self.players if p.life_point > 0]

        if len(players_in_life) > 0:
            self.players = players_in_life
        else :
            for player in self.players:
                player.add_life_point()
    
    def _check_winner(self):
        if len(self.players) == 1:
            return True
        return False
