from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from home_module.models import University, Country, City
from django.db.models import Q

class List_of_universities(ListView):
    template_name = ''
    model = University
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(List_of_universities, self).get_context_data(object_list=None, **kwargs)
        #search

        uni = University.objects.filter(Q(name__icontains=your_search_query))
        context['search_result_by_uniname'] = uni


        country = Country.objects.filter(Q(name__icontains=your_search_query)).first()
        if country:
            cities = country.city_set.all()
            if cities:
                for city in cities:
                    context['search_result_by_countryname']+= city.university_set.all()


        r_city = City.objects.filter(Q(name__icontains=your_search_query)).first().university_set.all()
        context['search_result_by_cityname'] = r_city

        #filter_by_country
        country_f = Country.objects.filter(id=id).first()
        if country_f:
            cities_f = country_f.city_set.all()
            if cities_f:
                for city in cities_f:
                    context['filter_result_by_country'] += city.university_set.all()

        # filter_by_city
        city_f = City.objects.filter(id=id).first()
        if city_f:
            context['filter_result_by_city'] =city_f.university_set.all()

        #Because I used listview, the list of universities can be accessed automatically in the html file


        return context


def University_info(request , id):
    university = University.objects.filter(id = id).first()
    context = {
        'name':university.name,
        'type':university.type,
        'overview':university.overview,
        'established_year':university.established_year,
        'number_of_students':university.number_of_students,
        'number_of_international_students':university.number_of_international_students,
        'url_uni_address':university.url_uni_address,
        'acceptance_rate':university.acceptance_rate,
        'logo':university.logo,
    }
    #Of course, We can only get the university itself and extract the rest of the items in the html file
    return render(request , template_name='' , context=context)