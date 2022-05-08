from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Category, Menu, Restaurant
from .serializers import *


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/category',
        'GET /api/category/:id',
        {
            'Endpoint': '/reservation/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'create new reservation with data send from post request',
        },
        'GET /api/restaurant',
        'GET /api/restaurant/:id',
        'GET /api/menu',
        'GET /api/menu/:id',
        'GET /api/table',
        'GET /api/table/:id',
        'GET /api/feedback',
        'GET /api/feedback/:id',
        'GET /api/reservation',
        'GET /api/reservation/:id',
        'GET /api/order_item',
        'GET /api/order_item/:id',
        'GET /api/order',
        'GET /api/order/:id',
    ]
    return Response(routes)

# category crud START .


@api_view(['GET'])
def getCategorys(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Item Deleted Successfuly')
# category crud END .

# restaurant crud START


@api_view(['GET'])
def getRestaurants(request):
    restaurant = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurant, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRestaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)
# restaurant crud END

# menu crud START .


@api_view(['GET'])
def getMenus(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    serializer = MenuSerializer(menu, many=False)
    return Response(serializer.data)
# menu crud END .

# table crud START .


@api_view(['GET'])
def getTables(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTable(request, pk):
    table = Table.objects.get(id=pk)
    serializer = TableSerializer(table, many=False)
    return Response(serializer.data)
# table crud END .

# call waiter crud START .


@api_view(['GET'])
def getCalls(request):
    call = Call_waiter.objects.all()
    serializer = CallWaiterSerializer(call, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createCall(request):
    serializer = CallWaiterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# call waiter crud END .

# reservation crud START .


@api_view(['GET'])
def getReservations(request):
    reservation = Reservation.objects.all()
    serializer = ReservationSerializer(reservation, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createReservation(request):
    serializer = ReservationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# reservation crud END .

# feedback crud START .


@api_view(['GET'])
def getFeedbacks(request):
    feedback = Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createFeedback(request):
    serializer = FeedbackSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# feedback crud END .

# order item crud START .


@api_view(['GET'])
def getOrderItems(request):
    feedback = Feedback.objects.all()
    serializer = OrderItemSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createOrderItem(request):
    serializer = OrderItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# order item crud END .

# order crud START .


@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# order crud END .
