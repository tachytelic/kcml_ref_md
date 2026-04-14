# Installing 32-Bit KCML 6 on 64-Bit Linux

KCML 6 ships as a 32-bit binary. On a 64-bit Linux host (e.g. Ubuntu 24.04 LTS) you must enable multiarch support and install the required 32-bit runtime libraries before the KCML interpreter will run.

---

## Step 1 — Enable i386 Architecture

```bash
sudo dpkg --add-architecture i386
sudo apt update
```

This tells `apt` to also resolve packages for the 32-bit x86 architecture.

---

## Step 2 — Install xinetd

KCML uses `xinetd` as its network service daemon. Install it before installing KCML:

```bash
sudo apt install xinetd
```

---

## Step 3 — Install Required 32-Bit Libraries

```bash
sudo apt install \
  libgcc-s1:i386 \
  libc6:i386 \
  libstdc++6:i386 \
  libpam0g:i386 \
  libncurses6:i386 \
  libtinfo6:i386 \
  libssl3t64:i386 \
  libcrypt1:i386
```

| Package | Purpose |
|---------|---------|
| `libc6:i386` | Core C runtime (glibc) |
| `libgcc-s1:i386` | GCC runtime support library |
| `libstdc++6:i386` | C++ standard library |
| `libpam0g:i386` | PAM authentication (used for login/session handling) |
| `libncurses6:i386` | Terminal/screen handling (ncurses) |
| `libtinfo6:i386` | Terminal info database (dependency of ncurses) |
| `libssl3t64:i386` | OpenSSL 3 TLS/crypto library |
| `libcrypt1:i386` | Password hashing and crypt(3) support |

---

## Step 4 — Add KCML to $PATH

Create a file in `/etc/profile.d/` so the KCML binaries are available system-wide:

```bash
sudo tee /etc/profile.d/kcml.sh > /dev/null << 'EOF'
export PATH="$PATH:/usr/local/kcml"
EOF
```

The change takes effect on next login, or immediately in the current shell with:

```bash
source /etc/profile.d/kcml.sh
```

---

## Verification

After installation, confirm the KCML interpreter loads without missing-library errors:

```bash
LD_PRELOAD=/usr/lib/kcml/ioctl_preload.so \
MAC_ADDRESS="00:0c:44:88:7a:4c" \
SPOOF_HOSTNAME="640UK" \
/usr/lib/kcml/kcml -p /tmp/test.kcml
```

If any library is still missing, `ldd` will show it:

```bash
ldd /usr/lib/kcml/kcml
```

Lines reading `not found` indicate additional 32-bit packages are needed.

---

## Notes

- The `t64` suffix on `libssl3t64:i386` is Ubuntu 24.04-specific — it indicates the 64-bit `time_t` transition build. Earlier Ubuntu releases use `libssl3:i386` instead.
- The `LD_PRELOAD`, `MAC_ADDRESS`, and `SPOOF_HOSTNAME` environment variables are required on every invocation of the KCML interpreter; see `README.md` and `CLAUDE.md` for the full execution pattern.
