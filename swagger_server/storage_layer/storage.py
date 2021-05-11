""" In memory 'DB' storage emulator for resources
    Good for testing purposes and other Mocking."""

# Constants
COMPANY_GROUP_NAME = 'companies'
OFFERS_GROUP_NAME = 'offers'
DISCOUNTCODES_GROUP_NAME = 'discountcodes'

# Storage in global variables. Not a clean or hidden solution.
# Replace with a Singleton pattern for an isolated name domain.
companies = {}
offers = {}
discountcodes = {}
resources_all = {
    COMPANY_GROUP_NAME: companies,
    OFFERS_GROUP_NAME: offers,
    DISCOUNTCODES_GROUP_NAME: discountcodes}
storage_counters = {
    COMPANY_GROUP_NAME: 0,
    OFFERS_GROUP_NAME: 0,
    DISCOUNTCODES_GROUP_NAME: 0}


def get_resource(resourceName: str, id: int):
    """ Get the data of a specified resource
        :param resourceName: Resource group name to add to
        :param id: Id of the resource to return
        :rtype: Dictionary with resource (id:resource dictionary)
            or None if not existing"""
    return resources_all[resourceName].get(id)


def get_resources(resourceName: str, filterfunc=None):
    """ Get all or a subset of resources for a specific resource group
        :param resourceName: Resource group name
        :param filterfunc:
            A filter function that gets two arguments when executed
            (id, resource dict). Expected to return True(include)
            or False (do not include)

        :rtype: Dictionary with resource id:resource dictionary
            with all known resources"""
    if filterfunc is None:
        return resources_all[resourceName]
    else:
        result = {}
        # Get the resource group and filter the items with the given function
        return {key: value for (key, value) in resources_all[resourceName].items() if filterfunc(key, value)}  # noqa: E501
        # Replaces
        # for key,value in resources_all[resourceName].items():
        #    if filterfunc(key,value):
        #        result[key]=value
        # return result


def search_resources(resourceName: str, criteria: {}=None):
    """ Search for resources fulfilling a set of given parameters.
        :param resourceName: Resource group name
        :param criteria: Dictionary with resource values to match
            If a criteria key (pair) cannot be excluded but should not be
            considered, use value as None => criteria is ignored.
        :rtype: Dictionary with resource id:resource dictionary
            with matching resources"""
    def filterfunc(id: int, resource: {})->bool:
        if criteria is not None:
            for key, value in criteria.items():
                # Criteria value None is ignored (may come from a default)
                if value is None:
                    continue  # Ignore this criteria
                # Key must exist in resource
                elif key not in resource:
                    return False  # Fail the total comparison
                # value in tested resource must match to continue
                elif key in resource and value != resource[key]:
                    return False  # Fail the total comparison
        # No failing matches with criteria so accept this resource
        return True
    return get_resources(resourceName, filterfunc)


def add_resource(resourceName: str, rsrc: {})->{}:
    """ Add a specific resource.
        If the same resource (id) already exists it is overwritten
        :param resourceName: Resource group name to add to
        :param rsrc: Dictionary with resource values
        :rtype: Dictionary with resource data (id:resource dictionary)"""
    result = rsrc.copy()  # Copy to avoid changing input
    if 'id' not in result or result['id'] is None:  # This is a new resource
        new_id = storage_counters[resourceName]
        result['id'] = new_id
        storage_counters[resourceName] += 1
    else:  # We are overwriting an existing resource
        # Make sure future resources are above the given id
        storage_counters[resourceName] = max(storage_counters[resourceName], result['id']+1)  # noqa: E501
    resources_all[resourceName].update({result['id']: result})
    # print(resources_all[resourceName])  # Good for debugging
    return result


def update_resource(resourceName: str, rsrc: {}):
    """ Modify a specific resource.
        If the same resource already exists it is modified,
        otherwise the new set is added with the given keys.
        Keys that are not included in the input resource dict are left
        untouched.
        :param resourceName: Resource group name to add to
        :param rsrc:
            Dictionary with resource values
            Id is is a mandatory key.
        :rtype: Dictionary with resource the updated resource
            (id:resource dictionary)"""
    # Create an id for new resources and update the newid counter
    if 'id' not in rsrc or rsrc['id'] is None:
        result = rsrc.copy()
        new_id = storage_counters[resourceName]
        result['id'] = new_id
        resources_all[resourceName].update({new_id: result})
        storage_counters[resourceName] += 1
    else:
        # Make sure future resources are above the given id
        storage_counters[resourceName] = max(storage_counters[resourceName], rsrc['id']+1)  # noqa: E501
        result = resources_all[resourceName][rsrc['id']]
        if result is None:
            result = rsrc.copy()
            resources_all[resourceName].update({rsrc['id']: result})
        else:
            result.update(rsrc)
    # print(resources_all[resourceName])  # Good for debugging
    return result


add_resource(COMPANY_GROUP_NAME, {'id': 0, 'name': 'companya'})
add_resource(COMPANY_GROUP_NAME, {'name': 'companyb', 'description': 'company b in germany'})  # noqa: E501
add_resource(COMPANY_GROUP_NAME, {'id': 4, 'name': 'companyc', 'description': 'c'})  # noqa: E501
