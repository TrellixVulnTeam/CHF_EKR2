# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427846916.452847
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/thankyou.html'
_template_uri = 'thankyou.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item_list2 = context.get('item_list2', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        product_list2 = context.get('product_list2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item_list2 = context.get('item_list2', UNDEFINED)
        def content():
            return render_content(context)
        product_list2 = context.get('product_list2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Thank You</h1>\n    \t<hr>\n\t</div>\n\n    <div class="container col-md-12">\n    <h3>Receipt for Payment</h3>\n')
        if product_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Product</th>\n                <th>Price</th>\n                <th>Quantity</th>\n            </tr>\n')
            for product in product_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/CannonFinished.jpg"></td>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.currentPrice))
                __M_writer('</td>\n                <td>')
                __M_writer(str(qty))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if item_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Price / day</th>\n                <th>Quantity</th>\n            </tr>\n')
            for item in item_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/Glasses.jpg"></td>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.STP))
                __M_writer('</td>\n                <td>')
                __M_writer(str(qty))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if rental_return:
            __M_writer('            <div><span>Damage Fee:</span> $')
            __M_writer(str(rental_return.damageFee))
            __M_writer('</div>\n            <br>\n            <div><span>Late Fee:</span> $')
            __M_writer(str(rental_return.lateFee))
            __M_writer('</div>\n            <br>\n            <div><span>Total Fee:</span> $')
            __M_writer(str(rental_return.totalFee))
            __M_writer('</div>\n')
        __M_writer('    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "thankyou.html", "line_map": {"64": 20, "65": 21, "66": 22, "67": 22, "68": 23, "69": 23, "70": 24, "71": 24, "72": 25, "73": 25, "74": 28, "75": 30, "76": 31, "77": 38, "78": 39, "79": 40, "80": 40, "81": 41, "82": 41, "83": 42, "84": 42, "85": 43, "86": 43, "87": 46, "88": 48, "89": 49, "90": 49, "27": 0, "92": 51, "93": 51, "94": 53, "95": 53, "96": 55, "91": 49, "102": 96, "39": 1, "44": 57, "50": 3, "61": 3, "62": 12, "63": 13}, "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/thankyou.html"}
__M_END_METADATA
"""
