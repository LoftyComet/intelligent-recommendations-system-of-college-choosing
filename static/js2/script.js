(function ($) {
    "use strict";
  
      
    $(window).on('scroll', function () {
      var window_top = $(window).scrollTop() + 1;
      if (window_top > 50) {
        $('.site-navigation').addClass('menu_fixed animated fadeInDown');
      } else {
        $('.site-navigation').removeClass('menu_fixed animated fadeInDown');
      }
    });
  
      // SCROLL TO TOP
      
      $(window).on('scroll', function () {
          if ($(window).scrollTop() > 70) {
              $('.scroll-to-top').addClass('reveal');
          } else {
              $('.scroll-to-top').removeClass('reveal');
          }
      });
  
  
   
  $('.testimonial-slider').slick({
          slidesToShow: 2,
          infinite: true,
          arrows: false,
          autoplay: true,
          autoplaySpeed: 4000,
          vertical:true,
          verticalSwiping:true
      });
  
   /* ---------------------------------------------
           owl-carousel
  --------------------------------------------- */
  
      $('.clients-carousel').owlCarousel({
          loop:false,
          margin:10,
          autoplay:true,
          nav:false,
          dots:false,
          responsive:{
              0:{
                  items:1,
              },
              600:{
                  items:3,
              },
              1000:{
                  items:5,
              }
          }
      })
  
   
      $('.review').owlCarousel({
          loop:true,
          margin:10,
          autoplay:false,
          nav:true,
          navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
          dots:false,
          responsive:{
              0:{
                  items:1,
              },
              600:{
                  items:3,
              },
              1000:{
                  items:2,
              }
          }
      })
  
  
      // Counter
  
      $('.counter').counterUp({
            delay: 10,
            time: 1000
        });
  
  
//   var form = $('.contact__form'),
//         message = $('.contact__msg'),
//         form_data;

//     // Success function
//     function done_func(response) {
//         message.fadeIn().removeClass('alert-danger').addClass('alert-success');
//         message.text(response);
//         setTimeout(function () {
//             message.fadeOut();
//         }, 2000);
//         form.find('input:not([type="submit"]), textarea').val('');
//     }

//     // fail function
//     function fail_func(data) {
//         message.fadeIn().removeClass('alert-success').addClass('alert-success');
//         message.text(data.responseText);
//         setTimeout(function () {
//             message.fadeOut();
//         }, 2000);
//     }
    
//     form.submit(function (e) {
//         e.preventDefault();
//         form_data = $(this).serialize();
//         $.ajax({
//             type: 'POST',
//             url: form.attr('action'),
//             data: form_data
//         })
//         .done(done_func)
//         .fail(fail_func);
//     });
      
  
  }(jQuery));