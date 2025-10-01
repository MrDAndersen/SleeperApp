from sleeper import SleeperBase

class SleeperLeague(SleeperBase):
  """
  Represents a league in the Sleeper API.

  Attributes:
      league_id (str): The unique identifier for the league.
      name (str): The name of the league.
      sport (str): The sport of the league (e.g., "NFL").
      status (str): The current status of the league.
      total_rosters (int): The total number of rosters in the league.
      roster_positions (list): The positions available in the league's rosters.
      previous_league_id (str): The ID of the previous league, if applicable.
      draft_id (str): The ID of the league's draft.
      settings (dict): The settings of the league.
      avatar (str): URL to the league's avatar image.
  """

  def __init__(self, league_id: str):
    super().__init__("NFL")
    league_info = self.send_request(f"/league/{str(league_id)}", None)

    self.total_rosters = league_info['data']['total_rosters']
    self.status = league_info['data']['status']
    self.sport = league_info['data']['sport']
    self.settings = league_info['data']['settings']
    self.roster_positions = league_info['data']['roster_positions']
    self.previous_league_id = league_info['data']['previous_league_id']
    self.name = league_info['data']['name']
    self.league_id = league_info['data']['league_id']
    self.draft_id = league_info['data']['draft_id']
    self.avatar = league_info['data']['avatar']
    if (self.sport != super().sport):
      super().__init__(self.sport)

  def rosters(self) -> dict:
    roster_path = self.update_path(f"/league/{self.league_id}/rosters")

    return (self.send_request(roster_path, None))

  def users(self) -> dict:
    user_path = self.update_path(f"/league/{self.league_id}/users")
    return (self.send_request(user_path, None))

  def drafts(self) -> dict:
    draft_path = self.update_path(f"/league/{self.league_id}/drafts")
    return (self.send_request(draft_path, None))

  def matchups(self, week: int) -> dict:
    matchup_path = self.update_path(f"/league/{self.league_id}/matchups/{week}")
    return (self.send_request(matchup_path, None))

  def winners_bracket(self) -> dict:
    bracket_path = self.update_path(f"/league/{self.league_id}/winners_bracket")
    return (self.send_request(bracket_path, None))

  def losers_bracket(self) -> dict:
    bracket_path = self.update_path(f"/league/{self.league_id}/losers_bracket")
    return (self.send_request(bracket_path, None))

  def transactions(self, week: int) -> dict:
    transaction_path = self.update_path(
      f"/league/{self.league_id}/transactions/{week}")
    return (self.send_request(transaction_path, None))

  def traded_picks(self) -> dict:
    picks_path = self.update_path(f"/league/{self.league_id}/traded_picks")
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
