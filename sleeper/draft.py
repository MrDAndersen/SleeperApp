# TODO: update to take into account that requests via SleeperBase returns both headers and data.
# TODO: make sure endpoint is correct for draft info

from sleeper import SleeperBase

class SleeperDraft(SleeperBase):

  def __init__(self, draft_id: str):
    super().__init__("NFL")
    self.base_url = super().update_path("draft/")

    info_url = self.update_path(str(draft_id))
    draft_info = self.send_request(info_url, None)
    self.type = draft_info["type"]
    self.status = draft_info["status"]
    self.sport = draft_info["sport"]
    self.settings = draft_info["settings"]
    self.season_type = draft_info["season_type"]
    self.season = draft_info["season"]
    self.metadata = draft_info["metatdata"]
    self.league_id = draft_info["league_id"]
    self.last_picked = draft_info["last_picked"]
    self.last_message_time = draft_info["last_message_time"]
    self.last_message_id = draft_info["last_message_id"]
    self.draft_order = draft_info["draft_order"]
    self.slot_to_roster_id = draft_info["slot_to_roster_id"]
    self.draft_id = draft_info["draft_id"]
    self.creators = draft_info["creators"]
    self.created = draft_info["created"]

  def picks(self) -> dict:
    picks_url = self.update_path(f"{self.draft_id}/picks")
    return (self.send_request(picks_url, None))

  def traded_picks(self) -> dict:
    traded_picks_url = self.update_path(f"{self.draft_id}/traded_picks")
    return (self.send_request(traded_picks_url, None))
