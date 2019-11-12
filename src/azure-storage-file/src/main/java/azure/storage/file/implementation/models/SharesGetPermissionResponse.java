// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) AutoRest Code Generator.

package com.azure.storage.file.implementation.models;

import com.azure.core.http.HttpHeaders;
import com.azure.core.http.HttpRequest;
import com.azure.core.http.rest.ResponseBase;

/**
 * Contains all response data for the getPermission operation.
 */
public final class SharesGetPermissionResponse extends ResponseBase<ShareGetPermissionHeaders, SharePermission> {
    /**
     * Creates an instance of SharesGetPermissionResponse.
     *
     * @param request the request which resulted in this SharesGetPermissionResponse.
     * @param statusCode the status code of the HTTP response.
     * @param rawHeaders the raw headers of the HTTP response.
     * @param value the deserialized value of the HTTP response.
     * @param headers the deserialized headers of the HTTP response.
     */
    public SharesGetPermissionResponse(HttpRequest request, int statusCode, HttpHeaders rawHeaders, SharePermission value, ShareGetPermissionHeaders headers) {
        super(request, statusCode, rawHeaders, value, headers);
    }

    /**
     * @return the deserialized response body.
     */
    @Override
    public SharePermission getValue() {
        return super.getValue();
    }
}
