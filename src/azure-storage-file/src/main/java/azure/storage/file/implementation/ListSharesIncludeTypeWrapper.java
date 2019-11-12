// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) AutoRest Code Generator.

package com.azure.storage.file.implementation;

import com.azure.storage.file.implementation.models.ListSharesIncludeType;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlProperty;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;
import java.util.List;

/**
 * A wrapper around List&lt;ListSharesIncludeType&gt; which provides top-level metadata for serialization.
 */
@JacksonXmlRootElement(localName = "ListSharesIncludeType")
public final class ListSharesIncludeTypeWrapper {
    @JacksonXmlProperty(localName = "ListSharesIncludeType")
    private final List<ListSharesIncludeType> listSharesIncludeType;

    /**
     * Creates an instance of ListSharesIncludeTypeWrapper.
     *
     * @param listSharesIncludeType the list.
     */
    @JsonCreator
    public ListSharesIncludeTypeWrapper(@JsonProperty("ListSharesIncludeType") List<ListSharesIncludeType> listSharesIncludeType) {
        this.listSharesIncludeType = listSharesIncludeType;
    }

    /**
     * Get the List&lt;ListSharesIncludeType&gt; contained in this wrapper.
     *
     * @return the List&lt;ListSharesIncludeType&gt;.
     */
    public List<ListSharesIncludeType> items() {
        return listSharesIncludeType;
    }
}
