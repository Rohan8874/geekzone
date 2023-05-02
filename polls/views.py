from django.shortcuts import render, redirect

def home(request):
    return render(request, 'polls/home.html')





# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, logout, authenticate
# from django.contrib import messages
# from django.forms import inlineformset_factory

# from .models import Order
# from .forms import OrderForm, CreateUserForm

# def register(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)

#             return redirect('login')

#     context = {'form':form}
#     return render(request, 'polls/register.html', context)

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password =request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Username OR password is incorrect')

#     context = {}
#     return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     return redirect('login')

# @login_required(login_url='login')
# def home(request):
#     orders = Order.objects.all()
#     # orderFilter = OrderFilter(request.GET, queryset=orders)
#     # orders = orderFilter.qs
#     context = {'orders':orders}
#     return render(request, 'home.html', context)

# @login_required(login_url='login')
# def create_order(request):
#     OrderFormSet = inlineformset_factory(Order, fields=('product', 'status'), extra=5)
#     formset = OrderFormSet(queryset=Order.objects.none(),instance=request.user)
#     #form = OrderForm(initial={'customer':request.user})
#     if request.method == 'POST':
#         #form = OrderForm(request.POST)
#         formset = OrderFormSet(request.POST,instance=request.user)
#         if formset.is_valid():
#             formset.save()
#             return redirect('home')
#     context = {'formset':formset}
#     return render(request, 'order_form.html', context)

# @login_required(login_url='login')
# def update_order(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {'form':form}
#     return render(request, 'order_form.html', context)

# @login_required(login_url='login')
# def delete_order(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == "POST":
#         order.delete()
#         return redirect('home')
#     context = {'item':order}
#     return render(request, 'delete.html', context)
