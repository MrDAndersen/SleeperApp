# TODO: update to take into account that requests via SleeperBase returns both headers and data.
# TODO: make sure endpoint is correct for league info

from sleeper import SleeperBase


class SleeperLeague(SleeperBase):

  def __init__(self, league_id: str):
    super().__init__("NFL")
    self.base_url = super().update_path("league/")

    info_url = self.update_path(str(league_id))
    league_info = self.send_request(info_url, None)

    self.total_rosters = league_info["total_rosters"]
    self.status = league_info["status"]
    self.sport = league_info["sport"]
    self.settings = league_info["settings"]
    self.roster_positions = league_info["roster_positions"]
    self.previous_league_id = league_info["previous_league_id"]
    self.name = league_info["name"]
    self.league_id = league_info["league_id"]
    self.draft_id = league_info["draft_id"]
    self.avatar = league_info["avatar"]
    if (self.sport != super().sport):
      super().__init__(self.sport)

  def rosters(self) -> dict:
    roster_path = self.update_path(f"{self.league_id}/rosters")

    return (self.send_request(roster_path, None))

  def users(self) -> dict:
    user_path = self.update_path(f"{self.league_id}/users")
    return (self.send_request(user_path, None))

  def drafts(self) -> dict:
    draft_path = self.update_path(f"{self.league_id}/drafts")
    return (self.send_request(draft_path, None))

  def matchups(self, week: int) -> dict:
    matchup_path = self.update_path(f"{self.league_id}/matchups/{week}")
    return (self.send_request(matchup_path, None))

  def winners_bracket(self) -> dict:
    bracket_path = self.update_path(f"{self.league_id}/winners_bracket")
    return (self.send_request(bracket_path, None))

  def losers_bracket(self) -> dict:
    bracket_path = self.update_path(f"{self.league_id}/losers_bracket")
    return (self.send_request(bracket_path, None))

  def transactions(self, week: int) -> dict:
    transaction_path = self.update_path(
      f"{self.league_id}/transactions/{week}")
    return (self.send_request(transaction_path, None))

  def traded_picks(self) -> dict:
    picks_path = self.update_path(f"{self.league_id}/traded_picks")
    return (self.send_request(picks_path, None))
  
  def league_info(self) -> dict:
    return {
      "league_id": self.league_id,
      "name": self.name,
      "sport": self.sport,
      "status": self.status,
      "total_rosters": self.total_rosters,
      "roster_positions": self.roster_positions,
      "previous_league_id": self.previous_league_id,
      "draft_id": self.draft_id,
      "settings": self.settings,
      "avatar": self.avatar
    }
