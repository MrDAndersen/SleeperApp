from sleeper import SleeperBase


class League(SleeperBase):
  total_rosters = None
  status = None
  sport = None
  settings = {}
  season_type = None
  scoring_settings = {}
  roster_positions = {}
  previous_league_id = None
  name = None
  league_id = None
  draft_id = None
  avatar = None

  def __init__(self, league_id):
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

  def rosters(self):
    roster_path = self.update_path(f"{self.league_id}/rosters")

    return (self.send_request(roster_path, None))

  def users(self):
    user_path = self.update_path(f"{self.league_id}/users")
    return (self.send_request(user_path, None))

  def drafts(self):
    draft_path = self.update_path(f"{self.league_id}/drafts")
    return (self.send_request(draft_path, None))

  def matchups(self, week):
    matchup_path = self.update_path(f"{self.league_id}/matchups/{week}")
    return (self.send_request(matchup_path, None))

  def winners_bracket(self):
    bracket_path = self.update_path(f"{self.league_id}/winners_bracket")
    return (self.send_request(bracket_path, None))

  def losers_bracket(self):
    bracket_path = self.update_path(f"{self.league_id}/losers_bracket")
    return (self.send_request(bracket_path, None))

  def transactions(self, week):
    transaction_path = self.update_path(
      f"{self.league_id}/transactions/{week}")
    return (self.send_request(transaction_path, None))

  def traded_picks(self):
    picks_path = self.update_path(f"{self.league_id}/traded_picks")
    return (self.send_request(picks_path, None))
