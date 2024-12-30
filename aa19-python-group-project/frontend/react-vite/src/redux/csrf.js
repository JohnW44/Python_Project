export function getCsrfToken() {
  return document.cookie.split('; ')
    .find(row => row.startsWith('csrf_token='))
    ?.split('=')[1];
}

export async function csrfFetch(url, options = {}) {
  options.method = options.method || 'GET';
  options.headers = options.headers || {};
  options.credentials = 'include';

  if (options.method.toUpperCase() !== 'GET') {
    options.headers['Content-Type'] = 'application/json';
    const csrfToken = getCsrfToken();
    if (csrfToken) {
      options.headers['XSRF-TOKEN'] = csrfToken;
      options.headers['X-CSRFToken'] = csrfToken;
    }
  }

  const res = await fetch(url, options);
  if (res.status >= 400) {
    console.error('Response error:', await res.text());
  }
  return res;
}