Name:           clr-fwupd-hooks
Version:        1
Release:        5
License:        Apache-2.0
Summary:        Auto-update runner for fwupd
Url:            https://clearlinux.org/
Group:          base
Source0:        clr-fwupd-update
Source1:        clr-fwupd-update.service
Requires:       fwupd

%description
Auto-update runner for fwupd

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/bin/clr-fwupd-update
install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clr-fwupd-update.service
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/
ln -s ../clr-fwupd-update.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/clr-fwupd-update.service

%files
/usr/bin/clr-fwupd-update
/usr/lib/systemd/system/clr-fwupd-update.service
/usr/lib/systemd/system/update-triggers.target.wants/clr-fwupd-update.service
