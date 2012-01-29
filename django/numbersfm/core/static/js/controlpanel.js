(function($) {
    // ----------------------------------------
    // View Classes
    // ----------------------------------------
    var views = {};
    
    // Update status form
    views.UpdateStatusForm = function($el) {
        var self = this;
        $el.find('#id_is_live').change(function() {
            self.updateInputs($(this).val());
        });

        self.updateInputs($el.find('#id_is_live').val());
    }

    views.UpdateStatusForm.prototype.updateInputs = function(val) {
        if(val == "False") {
            $el.find('#id_current_show').attr('disabled','disabled');
            $el.find('#id_current_song').attr('disabled','disabled');
        } else {
            $el.find('#id_current_show').removeAttr('disabled');
            $el.find('#id_current_song').removeAttr('disabled');
        }
    }
        
    // ---
    
    // ----------------------------------------    
    // Init
    // ----------------------------------------    
    $(function() {
        // `view_map` is like a dictionary of selectors -> functions
        // Each element matching each keyed selector has the value
        // function instantiated with the element as the only argument.
        // This is just an ultralight architecture for instantiating js
        // views from invidvidual DOM elements when they're present on
        // the page.
        var view_map = {
            '.update-status-form': views.UpdateStatusForm
        };

        for(var selector in view_map) {
            $(selector).each(function() {
                new view_map[selector]($(this));
            });
        }
    });
})(jQuery);