// Utilities

export default {

    doHttpGETFeroJson: async function (apiPath, params={}, headers={}, body=null) {
        let response = await this.doHttpGETJson(apiPath, params, headers, body)
        return response.body;
    },

    doHttpGETJson: async function (apiPath, params={}, headers={}, body=null) {
        let response = await this.doHttpGET(apiPath, params, headers, body)
        return response.json();
    },

    doHttpGETText: async function (apiPath, params={}, headers={}, body=null) {
        let response = await this.doHttpGET(apiPath, params, headers, body)
        return response.text();
    },
    doHttpAndEmitOnError: async function (url, fetchParams) {
        let response = null;
        try {
          response = await fetch(url, fetchParams);
          if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
          }
        } catch(err) {
            if ((response.status >= 500)||(response.status == 404)) {
              window.eventBus.emit("appFetchError", {
                url: url,
                fetchParams: fetchParams,
                httpStatus: response.status
              });
              throw err;
            }
            console.error(`${err} on ${url}`);
        };
        return response;
    },
    doHttpGET: async function (apiPath, params={}, headers={}, body=null) {
        
        let url = new URL(apiPath, window.settings.API_BASE_URL);
        for (const [name, value] of Object.entries(params)) {
          url.searchParams.set(name, value);
        }
        //headers['Authorization'] = `Bearer ${this.token}`;

        let fetchParams = {
            method: "GET",
            headers: headers,
            body: body
        };
        const response = await this.doHttpAndEmitOnError(url, fetchParams);
        return response;
    },
    doHttpDownload: function (apiPath, params={}, headers={}, body=null) {
        
        let url = new URL(apiPath, window.settings.API_BASE_URL);
        for (const [name, value] of Object.entries(params)) {
          url.searchParams.set(name, value);
        }
        //headers['Authorization'] = `Bearer ${this.token}`;

        window.location.href = url.href;
    },

    doHttpWrite: async function (apiPath, method="POST", params={}, headers={}, body=null) {
        
        let url = new URL(apiPath, window.settings.API_BASE_URL);
        for (const [name, value] of Object.entries(params)) {
          url.searchParams.set(name, value);
        }
        headers['Content-type'] = `application/json`;

        // Set csrf token
        let csrf_token = document.cookie.substring(
            document.cookie.indexOf("csrftoken=")+"csrftoken=".length);
        if (csrf_token.indexOf(";") != -1)
            csrf_token = csrf_token.substring(0, csrf_token.indexOf(";"));
        headers['X-CSRFToken'] = csrf_token;

        let fetchParams = {
            method: method,
            headers: headers,
            body: JSON.stringify(body)
        };
        const response = await this.doHttpAndEmitOnError(url, fetchParams);
        return response;
    }
}
