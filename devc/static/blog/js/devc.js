/* search
 * ------------------------------------------------------ */
var ssSearch = function () {
    searchWrap.on('click', function (e) {
        if ($(e.target).is('.search-field')) {
            closeSearch.trigger('click');
        }
    });
    searchField.attr({
        placeholder: 'Type Keywords',
        autocomplete: 'on'
    });

};

const year = new Date();
document.getElementById("getYear").textContent = year.getFullYear();