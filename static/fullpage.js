$(document).ready(function() {
    $('#fullpage').fullpage({
        sectionsColor: ['#f2f2f2', '#71cccd', '#7BAABE', 'whitesmoke', '#000'],
        navigation: true,
        slidesNavigation: true,
        controlArrows: false,
        anchors: ['search', 'company', 'thirdSection', 'fourthSection', 'fifthSection'],
        afterLoad: function(anchorLink, index) {
            $('.bubbles').hide();
            if (index == 2) {
                $('.bubbles').show();
              }
        },

        onLeave: function(index, nextIndex, direction) {
            if(index == 2) {
              $('.bubbles').hide();
            }
        },
    });
});