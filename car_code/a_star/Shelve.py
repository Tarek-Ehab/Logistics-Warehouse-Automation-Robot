import sys , os
import time 
# setting path
sys.path.append(os.path.dirname(sys.path[0]))
from decimal import Decimal
from a_star.testv3 import get_data
import a_star.testv3 as testv3




Shelve = {
    'One': 'D',
    'Two': 'B',
    'Three':'E',
    'Four':'G',
    'Five':'I',
    'Six':'G',
    'Seven':'J',
    'Eight':'L',
    'Nine':'E',
    'Ten':'J'

}


    
def Pickup_Orientation(goal,shelF):
    if ((goal =='E' and shelF== 'Nine') or (goal =='J' and shelF== 'Ten') or goal in('D' ,'I')) and testv3.car_orientaion == 'U':
        return 'R'
    elif ((goal =='E' and shelF== 'Nine') or (goal =='J' and shelF== 'Ten') or goal in('D' ,'I')) and testv3.car_orientaion == 'D':
        return 'L'
    elif ((goal =='G' and shelF== 'Six') or  goal == 'B') and testv3.car_orientaion ==  'R':
        return 'R'
    elif ((goal =='G' and shelF== 'Six') or  goal == 'B') and testv3.car_orientaion == 'L':
        return 'L'
    elif ((goal =='J' and shelF== 'Seven') or  (goal =='E' and shelF== 'Three')) and testv3.car_orientaion == 'U':
        return 'L'
    elif ((goal =='J' and shelF== 'Seven') or  (goal =='E' and shelF== 'Three')) and testv3.car_orientaion == 'D':
        return 'R'
    elif ((goal =='G' and shelF== 'Four') or goal == 'L') and testv3.car_orientaion == 'R':
        return 'L'
    elif ((goal =='G' and shelF== 'Four') or goal == 'L') and testv3.car_orientaion == 'L':
        return 'R'

def get_path_data(pickup_shelf, delevering_shelf,current_postoin):
    pickup_path = get_data(current_postoin, Shelve[pickup_shelf])
    pickup_data = [pickup_path,testv3.car_orientaion , Pickup_Orientation(Shelve[pickup_shelf],pickup_shelf),Shelve[pickup_shelf]]
    delever_path = get_data(Shelve[pickup_shelf],Shelve[delevering_shelf])
    delever_data = [delever_path , testv3.car_orientaion, Pickup_Orientation(Shelve[delevering_shelf],delevering_shelf),Shelve[delevering_shelf]]
    return pickup_data , delever_data