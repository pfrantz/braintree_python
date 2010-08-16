from braintree.exceptions.braintree_error import BraintreeError

class ServerError(BraintreeError):
    """ Raised when the gateway raises an error.  Please contant support at support@getbraintree.com. """
    pass