from src.administration.models import LeaveRequest, LeaveStatus, LeaveType, Staff
from utils.options import StaffStatus


class LeaveReport:
    def __init__(self):
        self.staffs_on_leave = Staff.objects.filter(status=StaffStatus.ON_LEAVE)
        self.leaves = LeaveRequest.objects.all()
    
    def __approved_leaves(self):
        approved_leaves = {}
        _leaves = self.leaves.filter(status=LeaveStatus.APPROVED).all()
        
        for leave in _leaves:
            approved_leaves["approved_leaves"] = [leave]
            approved_leaves["staffs"] = [leave.staff]
        return approved_leaves

    def leaves_on_progress(self) -> int:
        return self.staffs_on_leave.count()